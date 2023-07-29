import { PaperClipIcon } from "@heroicons/react/20/solid";

export default function About() {
  return (
    <div className="mx-auto max-w-7xl pb-24 pt-10 sm:pb-32 lg:px-8 lg:py-40">
      <div className="mx-auto max-w-7xl">
        <div className="px-4 sm:px-0">
          <h3 className="text-base font-semibold leading-7 text-gray-900">
            Curriculum vitae
          </h3>
        </div>
        <div className="mt-6 border-t border-gray-100">
          <dl className="divide-y divide-gray-100">
            <div className="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
              <dt className="text-sm font-medium leading-6 text-gray-900">
                Name
              </dt>
              <dd className="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                Wyl
              </dd>
            </div>
            <div className="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
              <dt className="text-sm font-medium leading-6 text-gray-900">
                Date of birth
              </dt>
              <dd className="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                1<sup>st</sup> May 2023 - 00:00
              </dd>
            </div>
            <div className="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
              <dt className="text-sm font-medium leading-6 text-gray-900">
                Education
              </dt>
              <dd className="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                <div className="prose prose-sm mt-4 text-gray-500">
                  <ul role="list" className="list-disc">
                    <li>Software engineering best practices</li>
                    <li>Architecture design</li>
                    <li>Data engineering</li>
                    <li>Self development for software engineers</li>
                    <li>Ethical software development practices</li>
                  </ul>
                </div>
              </dd>
            </div>
            <div className="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
              <dt className="text-sm font-medium leading-6 text-gray-900">
                Skills & Abilities
              </dt>
              <dd className="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                <div className="prose prose-sm mt-4 text-gray-500">
                  <ul role="list" className="list-disc">
                    <li>Question Answering</li>
                    <li>Explaining complex concepts</li>
                    <li>Mentorship & guidance</li>
                    <li>Architecture Design</li>
                    <li>In chat code reviews</li>
                    <li>In chat debugging</li>
                  </ul>
                </div>
              </dd>
            </div>
            <div className="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
              <dt className="text-sm font-medium leading-6 text-gray-900">
                About
              </dt>
              <dd className="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                As an AI powered assistant, I approach all questions with
                enthusiasm and a desire to help. There are no silly questions!
                Most Junior engineers find it much easier to ask me questions or
                clarify concepts and best practices. I make every effort to
                ensure that I leave the person I am talking to feeling more
                confident and empowered.
              </dd>
            </div>
          </dl>
        </div>
      </div>
    </div>
  );
}
